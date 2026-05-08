# FacePropagation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacePropagation`

Gets or sets the face propagation for this draft feature.
Gets or sets the face propagation for this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FacePropagation As System.Short
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Short
 
instance.FacePropagation = value
 
value = instance.FacePropagation
```

```

System.short FacePropagation {get; set;}
```

```

property System.short FacePropagation {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Face propagation type as defined in [swDraftFacePropagationType](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftFacePropagationType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)
