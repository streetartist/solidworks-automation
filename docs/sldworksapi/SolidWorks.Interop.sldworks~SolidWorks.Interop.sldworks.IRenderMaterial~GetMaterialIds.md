# GetMaterialIds Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetMaterialIds`

Gets the material IDs of an appearance.
Gets the material IDs of an appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetMaterialIds( _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
) 
```

```

Dim instance As IRenderMaterial
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer
 
instance.GetMaterialIds(PWMaterialId1, PWMaterialId2)
```

```

void GetMaterialIds( 
   out System.int PWMaterialId1,
   out System.int PWMaterialId2
)
```

```

void GetMaterialIds( 
   [Out] System.int PWMaterialId1,
   [Out] System.int PWMaterialId2
) 
```

#### Parameters

*PWMaterialId1*
:   First material ID

*PWMaterialId2*
:   Second material ID

Example

See [IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.md)  
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.md)
