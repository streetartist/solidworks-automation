# ConfigurationName Property (IDocumentSpecification)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ConfigurationName`

Gets or sets the name of the configuration to load when opening a model document.
Gets or sets the name of the configuration to load when opening a model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConfigurationName As System.String
```

```

Dim instance As IDocumentSpecification
Dim value As System.String
 
instance.ConfigurationName = value
 
value = instance.ConfigurationName
```

```

System.string ConfigurationName {get; set;}
```

```

property System.String^ ConfigurationName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of configuration to load

Remarks

This property is not valid for opening **3D**EXPERIENCE files using SOLIDWORKS Connected.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
