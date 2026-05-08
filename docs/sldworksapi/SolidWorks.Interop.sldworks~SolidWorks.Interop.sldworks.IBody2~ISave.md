# ISave Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISave`

Saves this body.
Saves this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISave( _
   ByVal StreamIn As System.Object _
) 
```

```

Dim instance As IBody2
Dim StreamIn As System.Object
 
instance.ISave(StreamIn)
```

```

void ISave( 
   System.object StreamIn
)
```

```

void ISave( 
   System.Object^ StreamIn
) 
```

#### Parameters

*StreamIn*
:   Stream to use for the save

Remarks

If you want to save the solid body associated with the document, then save the document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::Save Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Save.md)  
[IModeler::IRestore2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2.md)  
[IModeler::Restore Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~Restore.md)
