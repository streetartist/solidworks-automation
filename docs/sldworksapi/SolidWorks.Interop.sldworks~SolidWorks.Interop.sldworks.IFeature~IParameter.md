# IParameter Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter`

Gets a pointer to the object for the specified parameter or a pointer to the specified parameter.
Gets a pointer to the object for the specified parameter or a pointer to the specified parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IParameter( _
   ByVal Name As System.String _
) As Dimension
```

```

Dim instance As IFeature
Dim Name As System.String
Dim value As Dimension
 
value = instance.IParameter(Name)
```

```

Dimension IParameter( 
   System.string Name
)
```

```

Dimension^ IParameter( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of parameter (for example, "D1")

#### Return Value

[Dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)

Remarks

Most parameters are [dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md).

The Name argument for this method does not have to be the "full" dimension name. For example, you only need to pass "D1" not "D1@Base-Revolve". The full dimension name is required if you call [IModelDoc2::IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.md).

SOLIDWORKS recognizes some characters as special characters. The use of these characters in part or feature names can cause this method to fail and not return a dimension. These special characters are not recognized in names of parts or features:

- at sign ( @ )
- period ( . )
- backslash ( / )

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.md)  
[IModelDoc2::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.md)  
[IDimension::FullName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName.md)
