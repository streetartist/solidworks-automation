# IGetNames Method (IDisplayStateSetting)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetNames`

Gets the display state names for this display state setting.
Gets the display state names for this display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNames( _
   ByVal DsNameCount As System.Integer _
) As System.String
```

```

Dim instance As IDisplayStateSetting
Dim DsNameCount As System.Integer
Dim value As System.String
 
value = instance.IGetNames(DsNameCount)
```

```

System.string IGetNames( 
   System.int DsNameCount
)
```

```

System.String^ IGetNames( 
   System.int DsNameCount
) 
```

#### Parameters

*DsNameCount*
:   Number of display state names

#### Return Value

- in-process, unmanaged C++: Pointer to an array display state names
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IDisplayStateSetting::GetNameCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetNameCount.md) to populate DsNameCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)  
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.md)  
[IDisplayStateSetting::Names Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.md)  
[IDisplayStateSetting::ISetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.md)
