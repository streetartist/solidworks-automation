# ReorderFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2`

Moves the specified feature to another location in the FeatureManager design tree of this part or assembly.
Moves the specified feature to another location in the FeatureManager design tree of this part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReorderFeature2( _
   ByVal FeatToMove As System.String, _
   ByVal TargetFeat As System.String, _
   ByVal MoveLocation As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FeatToMove As System.String
Dim TargetFeat As System.String
Dim MoveLocation As System.Integer
Dim value As System.Boolean
 
value = instance.ReorderFeature2(FeatToMove, TargetFeat, MoveLocation)
```

```

System.bool ReorderFeature2( 
   System.string FeatToMove,
   System.string TargetFeat,
   System.int MoveLocation
)
```

```

System.bool ReorderFeature2( 
   System.String^ FeatToMove,
   System.String^ TargetFeat,
   System.int MoveLocation
) 
```

#### Parameters

*FeatToMove*
:   Name of feature to move (see **Remarks**)

*TargetFeat*
:   Name of feature before or after which to move FeatureToMove

    - or -

    Name of folder; valid only if MoveLocation is swMoveLocation\_e.swMoveToFolder and FeatToMove is not a Cut list/Solid Bodies folder

    (see **Remarks**)

*MoveLocation*
:   Move type as defined by [swMoveLocation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveLocation_e.html) (see **Remarks**)

#### Return Value

True if feature moved successfully, false if not

Remarks

This method functions just like the now obsolete IModelDocExtension::ReorderFeature, but also supports reordering of cut list folders and cut list sub-weldment folders.

When reordering cut list folders and sub-weldment folders, the following restrictions apply:

- FeatToMove is a folder feature: cut list / solid body / sub-weldment folder; FeatToMove is not a cut list item/solid body.
- This method:
  - reorders solid folders in parts and assembly components.
  - is called after assigning a ModelDoc variable to the part or assembly component whose cut list folders you want to reorder.
  - only affects cut lists in the active configuration. To reorder a cut list folder in another configuration, you must make it active before calling this method.
  - returns false if you try to move of a cut list/solid body folder to the top using either MoveLocation = swMoveLocation\_e.swMoveToTop or MoveLocation = swMoveLocation\_e.swMoveBefore. For example, if TargetFeat is the top folder, then you cannot set MoveLocation to swMoveLocation\_e.swMoveBefore.

Example

'VBA

'This example demonstrates how to use this method to re-order folders in the Cut list/Solid Bodies folder.

' Preconditions:

' 1. Open *Public\_documents***\samples\tutorial\api\weldment\_box3.sldprt**.

' 2. Open an Immediate window.

' 3. Run/Debug the macro.

'

'Postconditions:

' 1. When the macro pauses, inspect the Cut list folder.

' 2. Observe the order of two new sub folders in the Cut list folder: **Sub-weldment2** comes before **Sub-weldment3**.

' 3. Press F5 to reorder these folders.

' 4. When the macro pauses, inspect the reordered folders: **Sub-weldment3** moves before **Sub-weldment2**.

' 5. Select a body or folder in the Cut list folder.

' 6. Press F5 to locate the selection's parent folder.

' 7. Inspect the Immediate window for the parent folder type and name (Type = "SolidBodyFolder" and Name = "Solid Bodies").

'

' NOTE: Do not save the model as it is used by other examples.

'=====================================================

Dim swApp As SldWorks.SldWorks

Dim myFeature As SldWorks.Feature

Dim Part As SldWorks.ModelDoc2

Dim swFolderFeat As SldWorks.Feature

Dim swFeatureMgr As SldWorks.FeatureManager

Dim swSelectionMgr As SldWorks.SelectionMgr

Dim swSelObj As Object

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Option Explicit

Sub main()

    Set swApp = Application.SldWorks

   

    Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Structural Member1[3]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Structural Member1[4]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Structural Member1[6]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Structural Member1[8]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Structural Member3[1]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Structural Member3[2]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

   

    Set myFeature = Part.FeatureManager.**InsertSubFolder**()

   

    boolstatus = Part.Extension.SelectByID2("Gusset1", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Gusset2", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Gusset3", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

    boolstatus = Part.Extension.SelectByID2("Gusset4", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)

   

    Set myFeature = Part.FeatureManager.**InsertSubFolder**()

   

    Stop '1. Inspect the order of cut list folders;

    '2. Press F5 to reorder the folders

   

    boolstatus = Part.Extension.**ReorderFeature2**("Sub-weldment2", "Sub-weldment3", swMoveLocation\_e.swMoveAfter)

    Stop '1. Inspect the new order of cut list folders;

    '2. Select a body or body folder in the cut list folder;

    '3. Press F5 to locate its parent folder

   

    Set swSelectionMgr = Part.SelectionManager

    Debug.Print "Selected Obj Type: " & swSelectionMgr.GetSelectedObjectType3(1, -1)

    Set swSelObj = swSelectionMgr.GetSelectedObject6(1, -1)

   

    ' Locate the parent folder  of the selection

    Set swFeatureMgr = Part.FeatureManager

    Set swFolderFeat = swFeatureMgr.**CutListFolderLocation**(swSelObj)

       

    If swFolderFeat Is Nothing Then

        Debug.Print "Please select a solid body/cut list item or solid body/cut list folder"

        Exit Sub

    End If

   

    Debug.Print "Parent folder Type: " & swFolderFeat.GetTypeName2 & " Name: " & swFolderFeat.Name

   

End Sub

Example

[Reorder Features (VBA)](Reorder_Features_Example_VB.htm)  
[Reorder Features (VB.NET)](Reorder_Features_Example_VBNET.htm)  
[Reorder Features (C#)](Reorder_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IPartDoc::ReorderFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.md)  
[IAssemblyDoc::ReorderComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)
