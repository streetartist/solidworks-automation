# Revolution Property (IHelixFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Revolution`

Gets or sets the number of revolutions for this helix feature.
Gets or sets the number of revolutions for this helix feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Revolution As System.Double
```

```

Dim instance As IHelixFeatureData
Dim value As System.Double
 
instance.Revolution = value
 
value = instance.Revolution
```

```

System.double Revolution {get; set;}
```

```

property System.double Revolution {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Number of revolutions (see **Remarks**)

Remarks

If the [helix is defined](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DefinedBy.md) as swHelixDefinedBy\_e.swHelixDefinedByHeightAndPitch, then you cannot change the number of revolutions in the helix.

You must specify a value greater than the previous region's revolution value and less than the next region's revolution value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)
