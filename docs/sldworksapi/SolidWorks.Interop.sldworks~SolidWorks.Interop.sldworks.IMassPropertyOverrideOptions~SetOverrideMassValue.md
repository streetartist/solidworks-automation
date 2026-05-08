# SetOverrideMassValue Method (IMassPropertyOverrideOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMassValue`

Overrides the calculated mass of the model currently being edited.
Overrides the calculated mass of the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideMassValue( _
   ByVal Value As System.Double _
) As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim Value As System.Double
Dim value As System.Boolean
 
value = instance.SetOverrideMassValue(Value)
```

```

System.bool SetOverrideMassValue( 
   System.double Value
)
```

```

System.bool SetOverrideMassValue( 
   System.double Value
) 
```

#### Parameters

*Value*
:   New mass value

#### Return Value

True if the mass is successfully overridden, false if not

Remarks

This method is valid only if [IMassPropertyOverrideOptions::OverrideMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMass.md) is set to true.

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::Mass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Mass.md)
