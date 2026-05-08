# SweepType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SweepType`

Gets the type of this sweep feature.
Gets the type of this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property SweepType As System.Integer
```

```

Dim instance As ISweepFeatureData
Dim value As System.Integer
 
value = instance.SweepType
```

```

System.int SweepType {get;}
```

```

property System.int SweepType {
   System.int get();
}
```

#### Property Value

Sweep type as defined in [swFeatureNameID\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureNameID_e.html):

- swFmSweep (swept boss)
- swFmSweepCut (swept cut)
- swRefSurface (swept surface)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)
