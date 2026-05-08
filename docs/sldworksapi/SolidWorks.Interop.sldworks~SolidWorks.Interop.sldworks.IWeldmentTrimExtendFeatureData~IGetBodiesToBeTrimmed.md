# IGetBodiesToBeTrimmed Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetBodiesToBeTrimmed`

Gets the bodies to trim.
Gets the bodies to trim.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBodiesToBeTrimmed( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IWeldmentTrimExtendFeatureData
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetBodiesToBeTrimmed(Count)
```

```

Body2 IGetBodiesToBeTrimmed( 
   System.int Count
)
```

```

Body2^ IGetBodiesToBeTrimmed( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of bodies to trim

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to trim (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple bodies to trim. Use [IWeldmentTrimExtendFeatureData::CornerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.md) to determine the type of corner.

Before calling this method, call [IWeldmentTrimExtendFeatureData::GetBodiesToBeTrimmedCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetBodiesToBeTrimmedCount.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)  
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.md)  
[IWeldmentTrimExtendFeatureData::ISetBodiesToBeTrimmed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetBodiesToBeTrimmed.md)  
[IWeldmentTrimExtendFeatureData::BodiesToBeTrimmed Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.md)
