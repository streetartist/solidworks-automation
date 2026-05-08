# GetRenderMaterialsCount2 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount2`

Gets the number of appearances applied to this component in the specified display states.
Gets the number of appearances applied to this component in the specified display states.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRenderMaterialsCount2( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Integer
```

```

Dim instance As IComponent2
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Integer
 
value = instance.GetRenderMaterialsCount2(DisplayStateOption, DisplayStateNames)
```

```

System.int GetRenderMaterialsCount2( 
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

```

System.int GetRenderMaterialsCount2( 
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

Number of appearances

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetRenderMaterials2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials2.md)
