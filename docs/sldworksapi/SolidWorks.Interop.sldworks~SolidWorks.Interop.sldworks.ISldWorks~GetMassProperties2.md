# GetMassProperties2 Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMassProperties2`

Gets the mass properties from the specified document for the specified configuration.
Gets the mass properties from the specified document for the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMassProperties2( _
   ByVal FilePathName As System.String, _
   ByVal ConfigurationName As System.String, _
   ByVal Accuracy As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ConfigurationName As System.String
Dim Accuracy As System.Integer
Dim value As System.Object
 
value = instance.GetMassProperties2(FilePathName, ConfigurationName, Accuracy)
```

```

System.object GetMassProperties2( 
   System.string FilePathName,
   System.string ConfigurationName,
   System.int Accuracy
)
```

```

System.Object^ GetMassProperties2( 
   System.String^ FilePathName,
   System.String^ ConfigurationName,
   System.int Accuracy
) 
```

#### Parameters

*FilePathName*
:   Document path and file name

*ConfigurationName*
:   Name of the configuration to use

*Accuracy*
:   - 0 = as is
    - 1 = default
    - 2 = maximum

#### Return Value

Array of doubles of size 13; last element is the accuracy at which mass properties are calculated

Remarks

You can get the density of the current SOLIDWORKS part using [ISldWorks::GetUserPreferenceDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.md) and swMaterialPropertyDensity. If the density has not been explicitly set by the user, then SOLIDWORKS uses 1.0. You can also derive the density of the body from the following calculation:

Density = ( Mass / Volume )

Consistent with all other functions, this method returns metric units unless otherwise specified.

If this [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object is an assembly, then any suppressed components are not included in the mass property analysis. See [IComponent2::GetSuppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md) to determine the state of each of the assembly components.

This method returns an empty array if mass properties are not calculated when saving the model. This is a system-level setting and is controlled by [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) and swUpdateMassPropsDuringSave.

NOTE: The calculated origin for the return values is based on the default coordinate systems of the IModelDoc2, not on the a selected coordinate system.

Example

[Get Mass Properties of Inactive Document (VBA)](Get_Mass_Properties_of_Inactive_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetMassProperties2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMassProperties2.md)  
[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)
