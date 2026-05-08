# DraftAngle Property (ICoreFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftAngle`

Gets or sets the angle of the draft for this core feature.
Gets or sets the angle of the draft for this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DraftAngle As System.Double
```

```

Dim instance As ICoreFeatureData
Dim value As System.Double
 
instance.DraftAngle = value
 
value = instance.DraftAngle
```

```

System.double DraftAngle {get; set;}
```

```

property System.double DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle of draft

Remarks

To set this property, [ICoreFeatureData::UseDraft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~UseDraft.md) must be true.

Example

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)  
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)  
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.md)  
[ICoreFeatureData::DraftOutward Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftOutward.md)
