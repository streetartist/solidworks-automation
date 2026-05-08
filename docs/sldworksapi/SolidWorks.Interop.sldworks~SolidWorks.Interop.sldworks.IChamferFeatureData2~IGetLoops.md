# IGetLoops Method (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetLoops`

Gets the loops to which a chamfer is applied.
Gets the loops to which a chamfer is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLoops( _
   ByVal Count As System.Integer _
) As Loop
```

```

Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim value As Loop
 
value = instance.IGetLoops(Count)
```

```

Loop IGetLoops( 
   System.int Count
)
```

```

Loop^ IGetLoops( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of loops

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IChamferFeatureData2::LoopCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~LoopCount.md) before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetLoops.md)
