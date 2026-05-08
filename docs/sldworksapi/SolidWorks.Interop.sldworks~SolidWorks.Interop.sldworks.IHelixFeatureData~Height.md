# Height Property (IHelixFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Height`

Gets or sets the height of this helix feature.
Gets or sets the height of this helix feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Height As System.Double
```

```

Dim instance As IHelixFeatureData
Dim value As System.Double
 
instance.Height = value
 
value = instance.Height
```

```

System.double Height {get; set;}
```

```

property System.double Height {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Height (see **Remarks**)

Remarks

If the [helix is defined](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DefinedBy.md) as swHelixDefinedBy\_e.swHelixDefinedByPitchAndRevolution, then you cannot change the height of the helix.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)
