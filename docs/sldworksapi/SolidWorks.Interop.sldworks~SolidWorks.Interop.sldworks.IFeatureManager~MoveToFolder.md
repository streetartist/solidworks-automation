# MoveToFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoveToFolder`

Moves the selected feature or folder in the Solid Bodies Feature Manager design tree structure to the specified folder in the Solid Bodies Feature Manager design tree structure.
Moves the selected feature or folder in the Solid Bodies Feature Manager design tree structure to the specified folder in the Solid Bodies Feature Manager design tree structure.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MoveToFolder( _
   ByVal MoveToFeat As System.String, _
   ByVal MoveFromFeat As System.String, _
   ByVal IsFolder As System.Boolean _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim MoveToFeat As System.String
Dim MoveFromFeat As System.String
Dim IsFolder As System.Boolean
Dim value As System.Boolean
 
value = instance.MoveToFolder(MoveToFeat, MoveFromFeat, IsFolder)
```

```

System.bool MoveToFolder( 
   System.string MoveToFeat,
   System.string MoveFromFeat,
   System.bool IsFolder
)
```

```

System.bool MoveToFolder( 
   System.String^ MoveToFeat,
   System.String^ MoveFromFeat,
   System.bool IsFolder
) 
```

#### Parameters

*MoveToFeat*
:   Folder to which to move feature

*MoveFromFeat*
:   Folder from which to move feature

*IsFolder*
:   True if feature is a folder, false if a feature

#### Return Value

True if feature is moved, false if not

Remarks

This method is specific to the Solid Bodies folder only; it does not work for components.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
