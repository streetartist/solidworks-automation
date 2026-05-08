# GetUserPreferenceDoubleValueRange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDoubleValueRange`

Gets the current document default user preference value, and the minimum and maximum valid document user preference values.
Gets the current document default user preference value, and the minimum and maximum valid document user preference values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserPreferenceDoubleValueRange( _
   ByVal UserPref As System.Integer, _
   ByRef Value As System.Double, _
   ByRef MinValue As System.Double, _
   ByRef MaxValue As System.Double _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim UserPref As System.Integer
Dim Value As System.Double
Dim MinValue As System.Double
Dim MaxValue As System.Double
Dim value As System.Integer
 
value = instance.GetUserPreferenceDoubleValueRange(UserPref, Value, MinValue, MaxValue)
```

```

System.int GetUserPreferenceDoubleValueRange( 
   System.int UserPref,
   out System.double Value,
   out System.double MinValue,
   out System.double MaxValue
)
```

```

System.int GetUserPreferenceDoubleValueRange( 
   System.int UserPref,
   [Out] System.double Value,
   [Out] System.double MinValue,
   [Out] System.double MaxValue
) 
```

#### Parameters

*UserPref*
:   User preference as defined in [swUserPreferenceDoubleValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceDoubleValue_e.html)

*Value*
:   Current value of UserPref; if the return value >= 0, see **Remarks**

*MinValue*
:   Minimum value of UserPref; if the return value = 0, see Remarks

*MaxValue*
:   Maximum value of UserPref; if the return value= 0, see Remarks

#### Return Value

Status upon return from this method; see Remarks

Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS software.

The return value indicates the status upon return from this method:

- 0 indicates that the current, minimum, and maximum user preference values were retrieved.
- 1 indicates that the current user preference value was retrieved, but the minimum and maximum user preference values were not.  This most likely occurred because the SOLIDWORKS API code was not implemented to retrieve the minimum and maximum allowed values, so the return value is warning you that not all information was returned. It does not indicate a fatal error. The SOLIDWORKS API code is only implemented for returning the minimum and maximum value in cases where those values are not obvious to the user, such as with user preference swImageQualityShadedDeviation.
- -1 indicates that the current user preference value could not be retrieved. This most likely occurred because UserPref was not recognized as a valid user preference value.

If you want to retrieve the current user preference value only (i.e., you do not want to retrieve the valid minimum and maximum user preference values), use [IModelDocExtension::GetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ISldWorks::GetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.md)  
[ISldWorks::GetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceIntegerValue.md)  
[ISldWorks::GetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringListValue.md)  
[ISldWorks::GetUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.md)  
[ISldWorks::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md)  
[ISldWorks::SetUserPreferenceDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceDoubleValue.md)  
[ISldWorks::SetUserPreferenceIntegerValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.md)  
[ISldWorks::SetUserPreferenceStringListValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringListValue.md)  
[ISldWorks::SetUserPreferenceStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.md)  
[ISldWorks::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)  
[IModelDocExtension::GetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.md)  
[IModelDocExtension::GetUserPreferenceInteger Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md)  
[IModelDocExtension::GetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceString.md)  
[IModelDocExtension::GetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceTextFormat.md)  
[IModelDocExtension::GetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.md)  
[IModelDocExtension::SetUserPreferenceDouble Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.md)  
[IModelDocExtension::SetUserPreferenceInteger Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md)  
[IModelDocExtension::SetUserPreferenceString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceString.md)  
[IModelDocExtension::SetUserPreferenceTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceTextFormat.md)  
[IModelDocExtension::SetUserPreferenceToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.md)
