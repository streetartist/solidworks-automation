# InsertSubWeldFolder2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder2`

Creates a sub weld folder feature containing the specified weldment bodies.
Creates a sub weld folder feature containing the specified weldment bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSubWeldFolder2( _
   ByVal BodyArray As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BodyArray As System.Object
Dim value As Feature
 
value = instance.InsertSubWeldFolder2(BodyArray)
```

```

Feature InsertSubWeldFolder2( 
   System.object BodyArray
)
```

```

Feature^ InsertSubWeldFolder2( 
   System.Object^ BodyArray
) 
```

#### Parameters

*BodyArray*
:   Array of [Body2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) objects

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)  
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)  
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertSubWeldFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSubWeldFolder.md)
