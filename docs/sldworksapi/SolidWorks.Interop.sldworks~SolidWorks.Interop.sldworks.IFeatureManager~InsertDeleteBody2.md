# InsertDeleteBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDeleteBody2`

Inserts a Body-Delete/Keep feature.
Inserts a Body-Delete/Keep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertDeleteBody2( _
   ByVal KeepBodies As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim KeepBodies As System.Boolean
Dim value As Feature
 
value = instance.InsertDeleteBody2(KeepBodies)
```

```

Feature InsertDeleteBody2( 
   System.bool KeepBodies
)
```

```

Feature^ InsertDeleteBody2( 
   System.bool KeepBodies
) 
```

#### Parameters

*KeepBodies*
:   True to keep bodies, false to delete bodies

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Insert Body-Delete/Keep Feature (VBA)](Insert_Delete_Body_Feature_Example_VB.htm)  
[Insert Body-Delete/Keep Feature (VB.NET)](Insert_Delete_Body_Feature_Example_VBNET.htm)  
[Insert Body-Delete/Keep Feature (C#)](Insert_Delete_Body_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md)
