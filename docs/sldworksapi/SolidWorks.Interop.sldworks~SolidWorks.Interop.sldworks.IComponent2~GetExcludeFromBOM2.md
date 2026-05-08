# GetExcludeFromBOM2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetExcludeFromBOM2`

Gets whether this component is excluded from the bills of materials (BOMs) in the specified configurations.
Gets whether this component is excluded from the bills of materials (BOMs) in the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExcludeFromBOM2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object
 
value = instance.GetExcludeFromBOM2(Config_opt, Config_names)
```

```

System.object GetExcludeFromBOM2( 
   System.int Config_opt,
   System.object Config_names
)
```

```

System.Object^ GetExcludeFromBOM2( 
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of the names of configurations in whose BOMs this component is excluded or included; null or Nothing if Config\_opt is set to swInConfigurationOpts\_e.swAllConfiguration or swInConfigurationOpts\_e.swThisConfiguration

#### Return Value

Array of values indicating whether this component is:

- excluded (true) from

    - or -

- included (false) in

the BOMs of the specified configurations.

Remarks

This method is valid only for [table-based bills of materials](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md); it does not work for Microsoft Excel-based bills of materials.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::CompConfigProperties6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties6.md)  
[IComponent2::SetExcludeFromBOM2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetExcludeFromBOM2.md)
