# IGetParameters Method (IMacroFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParameters`

Gets the user-defined parameters.
Gets the user-defined parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetParameters( _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamTypes As System.Integer, _
   ByRef ParamValues As System.String _
) 
```

```

Dim instance As IMacroFeatureData
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamTypes As System.Integer
Dim ParamValues As System.String
 
instance.IGetParameters(ParamCount, ParamNames, ParamTypes, ParamValues)
```

```

void IGetParameters( 
   System.int ParamCount,
   out System.string ParamNames,
   out System.int ParamTypes,
   out System.string ParamValues
)
```

```

void IGetParameters( 
   System.int ParamCount,
   [Out] System.String^ ParamNames,
   [Out] System.int ParamTypes,
   [Out] System.String^ ParamValues
) 
```

#### Parameters

*ParamCount*
:   Number of user-defined parameters

*ParamNames*
:   - in-process, unmanaged C++: Pointer to an array of parameter names of size ParamCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*ParamTypes*
:   - in-process, unmanaged C++: Pointer to an array of parameter data types of size paramCount as defined in [swMacroFeatureParamType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureParamType_e.html)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*ParamValues*
:   - in-process, unmanaged C++: Pointer to an array of parameter values of size ParamCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IMacroFeatureData::GetParameterCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameterCount.md) to determine the size of the arrays.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetDoubleByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDoubleByName.md)  
[IMacroFeatureData::GetIntegerByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIntegerByName.md)  
[IMacroFeatureData::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParameters.md)  
[IMacroFeatureData::GetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetStringByName.md)  
[IMacroFeatureData::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParameters.md)  
[IMacroFeatureData::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetParameters.md)  
[IMacroFeatureData::SetStringByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetStringByName.md)
