# DPartDocEvents_ModifyTableNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ModifyTableNotifyEventHandler`

Notifies your program when a table has been modified in a part.
Notifies your program when a table has been modified in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_ModifyTableNotifyEventHandler( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As System.Integer, _
   ByVal reason As System.Integer, _
   ByVal RowInfo As System.Integer, _
   ByVal ColumnInfo As System.Integer, _
   ByVal DataInfo As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_ModifyTableNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_ModifyTableNotifyEventHandler( 
   TableAnnotation TableAnnotation,
   System.int TableType,
   System.int reason,
   System.int RowInfo,
   System.int ColumnInfo,
   System.string DataInfo
)
```

```

public delegate System.int DPartDocEvents_ModifyTableNotifyEventHandler( 
   TableAnnotation^ TableAnnotation,
   System.int TableType,
   System.int reason,
   System.int RowInfo,
   System.int ColumnInfo,
   System.String^ DataInfo
)
```

#### Parameters

*TableAnnotation*
:   [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)

*TableType*
:   Type of table as defined in [swTableAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

*reason*
:   Reason as defined in [swModifyTableNotifyReason\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swModifyTableNotifyReason_e.html)

*RowInfo*
:   Index of modified row

*ColumnInfo*
:   Index of modified column

*DataInfo*
:   Modified string

Remarks

If developing a C++ application, use [swPartModifyTableNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Fire Notification When Changing a Table in a Part Document (C#)](Fire_Notification_When_Changing_a_Table_in_a_Part_Document_Example_CSharp.htm)  
[Fire Notification When Changing a Table in a Part Document (VB.NET)](Fire_Notification_When_Changing_a_Table_in_a_Part_Document_Example_VBNET.htm)  
[Fire Notification When Changing a Table in a Part Document (VBA)](Fire_Notification_When_Changing_a_Table_in_a_Part_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_ModifyTableNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ModifyTableNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
