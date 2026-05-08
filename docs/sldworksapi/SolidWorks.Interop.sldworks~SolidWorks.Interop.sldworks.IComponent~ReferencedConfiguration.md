# ReferencedConfiguration Property (IComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~ReferencedConfiguration`

Obsolete. Superseded by IComponent2::ReferencedConfiguration.
Obsolete. Superseded by [IComponent2::ReferencedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencedConfiguration As System.String
```

```

Dim instance As IComponent
Dim value As System.String
 
instance.ReferencedConfiguration = value
 
value = instance.ReferencedConfiguration
```

```

System.string ReferencedConfiguration {get; set;}
```

```

property System.String^ ReferencedConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.md)  
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.md)
