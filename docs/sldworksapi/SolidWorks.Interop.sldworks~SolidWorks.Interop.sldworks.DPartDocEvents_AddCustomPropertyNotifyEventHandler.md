# DPartDocEvents_AddCustomPropertyNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AddCustomPropertyNotifyEventHandler`

Post-notifies the user program when the user has added a custom property.
Post-notifies the user program when the user has added a custom property.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_AddCustomPropertyNotifyEventHandler( _
   ByVal propName As System.String, _
   ByVal Configuration As System.String, _
   ByVal Value As System.String, _
   ByVal valueType As System.Integer _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_AddCustomPropertyNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_AddCustomPropertyNotifyEventHandler( 
   System.string propName,
   System.string Configuration,
   System.string Value,
   System.int valueType
)
```

```

public delegate System.int DPartDocEvents_AddCustomPropertyNotifyEventHandler( 
   System.String^ propName,
   System.String^ Configuration,
   System.String^ Value,
   System.int valueType
)
```

#### Parameters

*propName*
:   Name of the new custom property

*Configuration*
:   Configuration that contains the property

*Value*
:   Value of the new property

*valueType*
:   Valid type for VARIANT; see Microsoft MSDN for a list of valid VARIANT types

Remarks

If developing a C++ application, use [swPartAddCustomPropertyNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_AddCustomPropertyNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AddCustomPropertyNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
