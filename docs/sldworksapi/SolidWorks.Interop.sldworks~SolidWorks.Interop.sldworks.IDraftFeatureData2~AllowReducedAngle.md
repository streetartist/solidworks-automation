# AllowReducedAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~AllowReducedAngle`

Gets or sets the Allow reduced angle option for this draft feature.
Gets or sets the **Allow reduced angle** option for this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AllowReducedAngle As System.Boolean
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Boolean
 
instance.AllowReducedAngle = value
 
value = instance.AllowReducedAngle
```

```

System.bool AllowReducedAngle {get; set;}
```

```

property System.bool AllowReducedAngle {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reduce the angle of the draft, false to not

Remarks

See SOLIDWORKS Help for details about the **Allow reduced angle** setting.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~Angle.md)  
[IDraftFeatureData2::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetPartingLinesCount.md)  
[IDraftFeatureData2::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetPartingLines.md)  
[IDraftFeatureData2::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetPartingLines.md)  
[IDraftFeatureData2::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~PartingLines.md)  
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)
