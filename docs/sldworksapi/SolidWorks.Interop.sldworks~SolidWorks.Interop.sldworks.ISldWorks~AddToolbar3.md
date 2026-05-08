# AddToolbar3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar3`

Obsolete. Superseded by ISldWorks::AddToolbar4.
Obsolete. Superseded by [ISldWorks::AddToolbar4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToolbar3( _
   ByVal Cookie As System.Integer, _
   ByVal Title As System.String, _
   ByVal SmallBitmapResourceID As System.Integer, _
   ByVal LargeBitmapResourceID As System.Integer, _
   ByVal MenuPositionForToolbar As System.Integer, _
   ByVal DocumentType As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim Title As System.String
Dim SmallBitmapResourceID As System.Integer
Dim LargeBitmapResourceID As System.Integer
Dim MenuPositionForToolbar As System.Integer
Dim DocumentType As System.Integer
Dim value As System.Integer
 
value = instance.AddToolbar3(Cookie, Title, SmallBitmapResourceID, LargeBitmapResourceID, MenuPositionForToolbar, DocumentType)
```

```

System.int AddToolbar3( 
   System.int Cookie,
   System.string Title,
   System.int SmallBitmapResourceID,
   System.int LargeBitmapResourceID,
   System.int MenuPositionForToolbar,
   System.int DocumentType
)
```

```

System.int AddToolbar3( 
   System.int Cookie,
   System.String^ Title,
   System.int SmallBitmapResourceID,
   System.int LargeBitmapResourceID,
   System.int MenuPositionForToolbar,
   System.int DocumentType
) 
```

#### Parameters

*Cookie*

*Title*

*SmallBitmapResourceID*

*LargeBitmapResourceID*

*MenuPositionForToolbar*

*DocumentType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
