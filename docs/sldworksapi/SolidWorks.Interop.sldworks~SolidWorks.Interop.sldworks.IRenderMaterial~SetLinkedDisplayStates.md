# SetLinkedDisplayStates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetLinkedDisplayStates`

Sets the display states to which this appearance is applied.
Sets the display states to which this appearance is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLinkedDisplayStates( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Boolean
 
value = instance.SetLinkedDisplayStates(DisplayStateOption, DisplayStateNames)
```

```

System.bool SetLinkedDisplayStates( 
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

```

System.bool SetLinkedDisplayStates( 
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

True if display states successfully linked, false if not

Example

See the [IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetLinkedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetLinkedDisplayStates.md)
