# TaperOutward Property (IHelixFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~TaperOutward`

Gets or sets the direction of the taper for this constant-pitch helix feature.
Gets or sets the direction of the taper for this constant-pitch helix feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TaperOutward As System.Boolean
```

```

Dim instance As IHelixFeatureData
Dim value As System.Boolean
 
instance.TaperOutward = value
 
value = instance.TaperOutward
```

```

System.bool TaperOutward {get; set;}
```

```

property System.bool TaperOutward {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if outward, false if inward

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)
