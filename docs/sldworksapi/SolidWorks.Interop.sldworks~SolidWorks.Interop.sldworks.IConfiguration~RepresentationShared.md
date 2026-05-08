# RepresentationShared Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RepresentationShared`

Gets or sets whether this SOLIDWORKS Connected Representation configuration is shared.
Gets or sets whether this [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) Representation configuration is shared.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RepresentationShared As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.RepresentationShared = value
 
value = instance.RepresentationShared
```

```

System.bool RepresentationShared {get; set;}
```

```

property System.bool RepresentationShared {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this Representation configuration is shared, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
