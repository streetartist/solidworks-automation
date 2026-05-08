# IGetInterferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences`

Calculates and gets the interferences.
Calculates and gets the interferences.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetInterferences( _
   ByVal InterfernceCount As System.Integer _
) As Interference
```

```

Dim instance As IInterferenceDetectionMgr
Dim InterfernceCount As System.Integer
Dim value As Interference
 
value = instance.IGetInterferences(InterfernceCount)
```

```

Interference IGetInterferences( 
   System.int InterfernceCount
)
```

```

Interference^ IGetInterferences( 
   System.int InterfernceCount
) 
```

#### Parameters

*InterfernceCount*
:   Number of interferences

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [interferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IInterferenceDetectionMgr::GetInterferenceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceCount.md) to get the size of array for the interferences.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)  
[IInterferenceDetectionMgr::GetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.md)
