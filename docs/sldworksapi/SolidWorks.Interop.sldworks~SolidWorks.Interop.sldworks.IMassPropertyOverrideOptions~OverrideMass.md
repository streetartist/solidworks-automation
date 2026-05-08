# OverrideMass Property (IMassPropertyOverrideOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMass`

Gets or sets whether to override the calculated mass value for the model currently being edited.
Gets or sets whether to override the calculated mass value for the model currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideMass As System.Boolean
```

```

Dim instance As IMassPropertyOverrideOptions
Dim value As System.Boolean
 
instance.OverrideMass = value
 
value = instance.OverrideMass
```

```

System.bool OverrideMass {get; set;}
```

```

property System.bool OverrideMass {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the calculated mass value, false to not

Remarks

After setting this property to true, call [IMassPropertyOverrideOptions::SetOverrideMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMassValue.md).

Example

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassPropertyOverrideOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.md)  
[IMassPropertyOverrideOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.md)  
[IMassProperty2::Mass Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Mass.md)  
[IMassPropertyOverrideOptions::GetOverrideMassValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMassValue.md)
