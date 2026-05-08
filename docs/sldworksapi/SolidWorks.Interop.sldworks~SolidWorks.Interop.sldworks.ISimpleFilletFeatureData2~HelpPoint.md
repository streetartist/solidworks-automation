# HelpPoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint`

Gets or sets whether to resolve an ambiguous selection by using a help point when creating a face-face chamfer or a face fillet feature.
Gets or sets whether to resolve an ambiguous selection by using a help point when creating a face-face chamfer or a face fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HelpPoint As System.Object
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Object
 
instance.HelpPoint = value
 
value = instance.HelpPoint
```

```

System.object HelpPoint {get; set;}
```

```

property System.Object^ HelpPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Remarks

When creating a fillet or chamfer between two faces, it may not be clear where the blend should occur. Use this property to define the side of the fillet or chamfer that you want to blend. The fillet or chamfer is created at the location closest to the help point.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

NOTE:  This property corresponds to the Help point selection box that is available when creating face fillets or face-face chamfers. See the SOLIDWORKS user-interface help for more information about help points.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetHoldLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.md)  
[ISimpleFilletFeatureData2::IGetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.md)  
[ISimpleFilletFeatureData2::ISetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines.md)  
[ISimpleFilletFeatureData2::CurvatureContinuous Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.md)  
[ISimpleFilletFeatureData2::HoldLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.md)
