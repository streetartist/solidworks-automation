# SetProgId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetProgId`

Sets the version-independent program ID that is valid for this COM feature.
Sets the version-independent program ID that is valid for this COM feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetProgId( _
   ByVal ProgId As System.String _
) 
```

```

Dim instance As IMacroFeatureData
Dim ProgId As System.String
 
instance.SetProgId(ProgId)
```

```

void SetProgId( 
   System.string ProgId
)
```

```

void SetProgId( 
   System.String^ ProgId
) 
```

#### Parameters

*ProgId*
:   Name of the program ID for the component that implements the COM feature handler

Remarks

See [Exposed COM DLL or Executable and Macro Features](sldworksapiprogguide.chm::/Macro_Features/Exposed_COM_DLL_or_Executable.htm) for details about macro features that define their behavior using COM.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetProgId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProgId.md)  
[IMacroFeatureData::IsCOMFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IsCOMFeature.md)
