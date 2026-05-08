# ISetLoops Method (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetLoops`

Sets the loops to which a chamfer is applied.
Sets the loops to which a chamfer is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetLoops( _
   ByVal Count As System.Integer, _
   ByRef LoopList As Loop _
) 
```

```

Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim LoopList As Loop
 
instance.ISetLoops(Count, LoopList)
```

```

void ISetLoops( 
   System.int Count,
   ref Loop LoopList
)
```

```

void ISetLoops( 
   System.int Count,
   Loop^% LoopList
) 
```

#### Parameters

*Count*
:   Number of loops

*LoopList*
:   - in-process, unmanaged C++: Pointer to an array of [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetLoops.md)  
[IChamferFeatureData2::Loops Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Loops.md)
