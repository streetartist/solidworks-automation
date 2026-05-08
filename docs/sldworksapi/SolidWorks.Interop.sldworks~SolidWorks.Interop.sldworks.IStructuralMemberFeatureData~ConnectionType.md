# ConnectionType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType`

Gets or sets the type of corner treatment at the specified connection point of this structural member.
Gets or sets the type of corner treatment at the specified connection point of this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConnectionType( _
   ByVal AtPoint As SketchPoint _
) As System.Integer
```

```

Dim instance As IStructuralMemberFeatureData
Dim AtPoint As SketchPoint
Dim value As System.Integer
 
instance.ConnectionType(AtPoint) = value
 
value = instance.ConnectionType(AtPoint)
```

```

System.int ConnectionType( 
   SketchPoint AtPoint
) {get; set;}
```

```

property System.int ConnectionType {
   System.int get(SketchPoint^ AtPoint);
   void set (SketchPoint^ AtPoint, System.int value);
}
```

#### Parameters

*AtPoint*
:   [Connect point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

#### Property Value

Type of corner treatment as defined in [swSolidworksWeldmentEndCondOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)  
[IStructuralMemberFeatureData::ApplyCornerTreatment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.md)  
[IStructuralMemberFeatureData::CornerTreatmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.md)  
[IStructuralMemberFeatureData::GetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.md)  
[IStructuralMemberFeatureData::GetConnectionPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount.md)  
[IStructuralMemberFeatureData::IGetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.md)
