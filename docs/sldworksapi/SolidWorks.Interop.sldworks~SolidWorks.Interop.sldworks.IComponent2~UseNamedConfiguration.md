# UseNamedConfiguration Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UseNamedConfiguration`

Gets whether a specified configuration or the in-use/last active configuration is used.
Gets whether a specified configuration or the in-use/last active configuration is used.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property UseNamedConfiguration As System.Boolean
```

```

Dim instance As IComponent2
Dim value As System.Boolean
 
value = instance.UseNamedConfiguration
```

```

System.bool UseNamedConfiguration {get;}
```

```

property System.bool UseNamedConfiguration {
   System.bool get();
}
```

#### Property Value

True if a configuration is specified and used, false if the in-use/last active configuration is used

Remarks

Use [IAssemblyDoc::CompConfigProperties4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.md) to set this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
