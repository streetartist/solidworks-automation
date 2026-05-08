# IGetLoops Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetLoops`

Gets the loops on which to create a simple radius fillet.
Gets the loops on which to create a simple radius fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLoops( _
   ByVal Count As System.Integer _
) As Loop2
```

```

Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim value As Loop2
 
value = instance.IGetLoops(Count)
```

```

Loop2 IGetLoops( 
   System.int Count
)
```

```

Loop2^ IGetLoops( 
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

Call [ISimpleFilletFeatureData2::GetLoopCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetLoopCount.md) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetLoops.md)  
[ISimpleFilletFeatureData2::Loops Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Loops.md)
