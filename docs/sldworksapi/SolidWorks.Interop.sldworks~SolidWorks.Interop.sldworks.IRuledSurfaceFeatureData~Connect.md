# Connect Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~Connect`

Gets or sets whether or not to connect the surfaces of this ruled-surface feature.
Gets or sets whether or not to connect the surfaces of this ruled-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Connect As System.Boolean
```

```

Dim instance As IRuledSurfaceFeatureData
Dim value As System.Boolean
 
instance.Connect = value
 
value = instance.Connect
```

```

System.bool Connect {get; set;}
```

```

property System.bool Connect {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to connect surfaces, false to remove connecting surfaces

Remarks

Connecting surfaces are usually created between sharp corners.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.md)
