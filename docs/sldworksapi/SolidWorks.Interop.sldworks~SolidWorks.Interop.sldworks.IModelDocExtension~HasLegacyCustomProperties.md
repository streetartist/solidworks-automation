# HasLegacyCustomProperties Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCustomProperties`

Gets whether this model has legacy custom properties.
Gets whether this model has legacy custom properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property HasLegacyCustomProperties As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.HasLegacyCustomProperties
```

```

System.bool HasLegacyCustomProperties {get;}
```

```

property System.bool HasLegacyCustomProperties {
   System.bool get();
}
```

#### Property Value

True if the model has legacy custom properties, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
