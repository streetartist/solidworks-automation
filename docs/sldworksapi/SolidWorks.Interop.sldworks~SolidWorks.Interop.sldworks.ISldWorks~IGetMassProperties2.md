# IGetMassProperties2 Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMassProperties2`

Gets the mass properties from the specified document for the specified configuration.
Gets the mass properties from the specified document for the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMassProperties2( _
   ByVal FilePathName As System.String, _
   ByVal ConfigurationName As System.String, _
   ByRef MPropsData As System.Double, _
   ByVal Accuracy As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ConfigurationName As System.String
Dim MPropsData As System.Double
Dim Accuracy As System.Integer
Dim value As System.Boolean
 
value = instance.IGetMassProperties2(FilePathName, ConfigurationName, MPropsData, Accuracy)
```

```

System.bool IGetMassProperties2( 
   System.string FilePathName,
   System.string ConfigurationName,
   ref System.double MPropsData,
   System.int Accuracy
)
```

```

System.bool IGetMassProperties2( 
   System.String^ FilePathName,
   System.String^ ConfigurationName,
   System.double% MPropsData,
   System.int Accuracy
) 
```

#### Parameters

*FilePathName*
:   Document path and file name

*ConfigurationName*
:   Name of configuration to use

*MPropsData*
:   Array of doubles

*Accuracy*
:   - 0 = as is
    - 1 = default
    - 2 = maximum

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles of size 13; last element is the accuracy at which mass properties are calculated

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

You can get the density of the current SOLIDWORKS part using [ISldWorks::GetUserPreferenceDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.md) and swMaterialPropertyDensity. If the density has not been explicitly set by the user, then SOLIDWORKS uses 1.0. You can also derive the density of the body from the following calculation:

Density = ( Mass / Volume )

Consistent with all other functions, this method returns metric units unless otherwise specified.

If this [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object is an assembly, then any suppressed components are not included in the mass property analysis. See [IComponent2::GetSuppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md) to determine the state of each of the assembly components.

This method returns an empty array if mass properties are not calculated when saving the model. This is a system-level setting and is controlled by [ISldworks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) and swUpdateMassPropsDuringSave.

NOTE: The calculated origin for the return values is based on the default coordinate systems of the IModelDoc2, not on the a selected coordinate system.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[ISldWorks::GetMassProperties2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMassProperties2.md)
