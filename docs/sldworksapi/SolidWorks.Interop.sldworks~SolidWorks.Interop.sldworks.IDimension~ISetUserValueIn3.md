# ISetUserValueIn3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3`

Sets the value of this dimension in the units of the specified document.
Sets the value of this dimension in the units of the specified document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetUserValueIn3( _
   ByVal Doc As ModelDoc2, _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer _
) As System.Integer
```

```

Dim instance As IDimension
Dim Doc As ModelDoc2
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim value As System.Integer
 
value = instance.ISetUserValueIn3(Doc, NewValue, WhichConfigurations)
```

```

System.int ISetUserValueIn3( 
   ModelDoc2 Doc,
   System.double NewValue,
   System.int WhichConfigurations
)
```

```

System.int ISetUserValueIn3( 
   ModelDoc2^ Doc,
   System.double NewValue,
   System.int WhichConfigurations
) 
```

#### Parameters

*Doc*
:   [Document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) whose units you want to use

*NewValue*
:   Value for this dimension in the units of the document specified by Doc

*WhichConfigurations*
:   Configurations to set the value as defined in [swSetValueInConfiguration\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html)

#### Return Value

Success indicator as defined in [swSetValueReturnStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueReturnStatus_e.html)

Remarks

The WhichConfigs argument is equivalent to the **Change Parameter** dialog in the SOLIDWORKS user interface, which gives the user the option of having the value set in all configurations or the current configuration. If there is one configuration in the part, SOLIDWORKS ignores this argument.

This method allows you to change the value of a read-only dimension. You can use [IDimension::ReadOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReadOnly.md) to determine if a dimension is read-only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md)  
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md)  
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md)  
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.md)  
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.md)  
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.md)  
[IDimension::SetSystemValue2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue2.md)  
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.md)  
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md)  
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.md)
