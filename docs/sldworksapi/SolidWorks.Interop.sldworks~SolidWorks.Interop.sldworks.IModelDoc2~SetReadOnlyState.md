# SetReadOnlyState Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetReadOnlyState`

Sets whether this document is read-only or read-write.
Sets whether this document is read-only or read-write.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetReadOnlyState( _
   ByVal SetReadOnly As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim SetReadOnly As System.Boolean
Dim value As System.Boolean
 
value = instance.SetReadOnlyState(SetReadOnly)
```

```

System.bool SetReadOnlyState( 
   System.bool SetReadOnly
)
```

```

System.bool SetReadOnlyState( 
   System.bool SetReadOnly
) 
```

#### Parameters

*SetReadOnly*
:   True to set this document to be read-only, false to set this document to read-write

#### Return Value

True if method executes successfully, false if not

Remarks

If the file is opened as read-write, specifying read-only should work except if it is a new file that has not yet been saved.

If the file is opened as read-only in SOLIDWORKS, then specifying read-write only changes the internal SOLIDWORKS state (not the access rights on disk) and only succeeds if it would be possible to open this file with write access. If the file is read-only on disk or if another user has it open with write access, then this method does not change the internal state to writeable; the document remains read-only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IsOpenedReadOnly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedReadOnly.md)  
[IModelDoc2::IsOpenedViewOnly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.md)
