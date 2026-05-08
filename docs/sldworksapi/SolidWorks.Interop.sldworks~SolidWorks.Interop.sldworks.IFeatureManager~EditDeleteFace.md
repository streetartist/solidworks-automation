# EditDeleteFace Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditDeleteFace`

Edits a DeleteFace feature.
Edits a DeleteFace feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditDeleteFace( _
   ByVal Refill As System.Integer _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Refill As System.Integer
Dim value As System.Boolean
 
value = instance.EditDeleteFace(Refill)
```

```

System.bool EditDeleteFace( 
   System.int Refill
)
```

```

System.bool EditDeleteFace( 
   System.int Refill
) 
```

#### Parameters

*Refill*
:   1 refills the face after it is deleted

    0 does not

#### Return Value

True if the operation succeeds, false if not

Remarks

This method assumes that the new faces to delete and the [DeleteFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.md) feature are selected.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.md)  
[IModelDocExtension::InsertDeleteFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDeleteFace.md)
