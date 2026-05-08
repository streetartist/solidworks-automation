# InsertAnnotationView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAnnotationView`

Inserts an annotation view in this part or assembly document.
Inserts an annotation view in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertAnnotationView( _
   ByVal AnnotationViewingDirection As System.Integer, _
   ByVal DirectionReference As System.Object, _
   ByVal FlipDirection As System.Boolean, _
   ByVal HorizontalDirectionReference As System.Object, _
   ByVal AngleMadeWithHorizontal As System.Integer _
) As AnnotationView
```

```

Dim instance As IModelDocExtension
Dim AnnotationViewingDirection As System.Integer
Dim DirectionReference As System.Object
Dim FlipDirection As System.Boolean
Dim HorizontalDirectionReference As System.Object
Dim AngleMadeWithHorizontal As System.Integer
Dim value As AnnotationView
 
value = instance.InsertAnnotationView(AnnotationViewingDirection, DirectionReference, FlipDirection, HorizontalDirectionReference, AngleMadeWithHorizontal)
```

```

AnnotationView InsertAnnotationView( 
   System.int AnnotationViewingDirection,
   System.object DirectionReference,
   System.bool FlipDirection,
   System.object HorizontalDirectionReference,
   System.int AngleMadeWithHorizontal
)
```

```

AnnotationView^ InsertAnnotationView( 
   System.int AnnotationViewingDirection,
   System.Object^ DirectionReference,
   System.bool FlipDirection,
   System.Object^ HorizontalDirectionReference,
   System.int AngleMadeWithHorizontal
) 
```

#### Parameters

*AnnotationViewingDirection*
:   Defined by either any [swStandardViews\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html) enumerator or 0 for selection

*DirectionReference*
:   If 0 specified for AnnotationViewingDirection, then specifiy a [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) to define the direction of the annotation view

*FlipDirection*
:   True to flip the annotation view in the opposite direction, false to not

*HorizontalDirectionReference*
:   An [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), or [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*AngleMadeWithHorizontal*
:   Angle (in degrees) with the specified HorizontalDirectionReference

#### Return Value

Newly inserted [annotation view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)

Example

'VBA

'----------------------------------------------------------------------------

' Preconditions:

' 1. Open a SOLIDWORKS model file.

' 2. Select a face to define the direction of the annotation view.

' 3. Select an edge as a horizontal direction reference.

'

' Postconditions: Observe that a new annotation view is inserted at a 45 degree angle in reference to the face and edge.

'----------------------------------------------------------------------------

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModExt As SldWorks.ModelDocExtension

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFace As SldWorks.Face2

Dim swEdge As SldWorks.edge

Dim swAnnoView As SldWorks.AnnotationView

Dim i As Integer

Sub main()

     Set swApp = Application.SldWorks

     Set swModel = swApp.ActiveDoc

     Set swModExt = swModel.Extension

     Set swSelMgr = swModel.SelectionManager

     For i = 0 To swSelMgr.GetSelectedObjectCount2(-1) - 1

         If swSelMgr.GetSelectedObjectType3(i + 1, -1) = swSelFACES Then

             Set swFace = swSelMgr.GetSelectedObject6(i + 1, -1)

         End If

         If swSelMgr.GetSelectedObjectType3(i + 1, -1) = swSelEDGES Then

             Set swEdge = swSelMgr.GetSelectedObject6(i + 1, -1)

         End If

     Next i

   

     Set annoView = swModExt.**InsertAnnotationView**(0, Nothing, False, swEdge, 45)

     swModel.EditRebuild3

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
