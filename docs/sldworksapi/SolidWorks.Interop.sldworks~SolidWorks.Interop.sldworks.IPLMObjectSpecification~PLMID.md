# PLMID Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification~PLMID`

Gets or sets the ID of a SOLIDWORKS Connected document.
Gets or sets the ID of a [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm) document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PLMID As System.String
```

```

Dim instance As IPLMObjectSpecification
Dim value As System.String
 
instance.PLMID = value
 
value = instance.PLMID
```

```

System.string PLMID {get; set;}
```

```

property System.String^ PLMID {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Document ID

Example

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPLMObjectSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.md)  
[IPLMObjectSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification_members.md)
