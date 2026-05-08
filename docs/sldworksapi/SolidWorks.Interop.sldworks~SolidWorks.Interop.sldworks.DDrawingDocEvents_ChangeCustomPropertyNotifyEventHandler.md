# DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler`

Post-notifies the user program when the user has changed a custom property.
Post-notifies the user program when the user has changed a custom property.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler( _
   ByVal propName As System.String, _
   ByVal Configuration As System.String, _
   ByVal oldValue As System.String, _
   ByVal NewValue As System.String, _
   ByVal valueType As System.Integer _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler( 
   System.string propName,
   System.string Configuration,
   System.string oldValue,
   System.string NewValue,
   System.int valueType
)
```

```

public delegate System.int DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler( 
   System.String^ propName,
   System.String^ Configuration,
   System.String^ oldValue,
   System.String^ NewValue,
   System.int valueType
)
```

#### Parameters

*propName*
:   Name of the changed property

*Configuration*
:   Configuration that contains the property

*oldValue*
:   Previous value of the property

*NewValue*
:   New value of the property

*valueType*
:   Valid type for VARIANT; see Microsoft MSDN for a list of the valid VARIANT types

Remarks

The ValueType argument is one of the valid types that VARIANT can contain.

If developing a C++ application, use [swDrawingChangeCustomPropertyNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_ChangeCustomPropertyNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
