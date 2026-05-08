# GetRenderMaterials2 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials2`

Gets the appearances applied to this component in the specified display states.
Gets the appearances applied to this component in the specified display states.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRenderMaterials2( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Object
 
value = instance.GetRenderMaterials2(DisplayStateOption, DisplayStateNames)
```

```

System.object GetRenderMaterials2( 
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

```

System.Object^ GetRenderMaterials2( 
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames
) 
```

#### Parameters

*DisplayStateOption*
:   Display states as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)

*DisplayStateNames*
:   Array of display state names

#### Return Value

Array of [appearances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetRenderMaterialsCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount2.md)
