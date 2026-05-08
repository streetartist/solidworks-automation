# ISetHoldLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines`

Sets the hold lines (boundaries) for this face blend fillet feature.
Sets the hold lines (boundaries) for this face blend fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetHoldLines( _
   ByVal Count As System.Integer, _
   ByRef PList As System.Object _
) 
```

```

Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim PList As System.Object
 
instance.ISetHoldLines(Count, PList)
```

```

void ISetHoldLines( 
   System.int Count,
   ref System.object PList
)
```

```

void ISetHoldLines( 
   System.int Count,
   System.Object^% PList
) 
```

#### Parameters

*Count*
:   Number of hold lines

*PList*
:   - in-process, unmanaged C++: Pointer to an array of hold lines of size Count

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method corresponds to the Hold lines selection box available when creating face-blend fillets. See the SOLIDWORKS Help for more information about face-blend fillets and hold lines.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetHoldLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.md)  
[ISimpleFilletFeatureData2::IGetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.md)  
[ISimpleFilletFeatureData2::HoldLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.md)  
[ISimpleFilletFeatureData2::CurvatureContinuous Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.md)  
[ISimpleFilletFeatureData2::HelpPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.md)
