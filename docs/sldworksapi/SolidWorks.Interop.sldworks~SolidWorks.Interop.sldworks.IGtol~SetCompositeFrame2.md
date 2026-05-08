# SetCompositeFrame2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetCompositeFrame2`

Sets whether to create a composite frame containing the specified GTol frame.
Sets whether to create a composite frame containing the specified GTol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCompositeFrame2( _
   ByVal Composite As System.Boolean, _
   ByVal FrameNum As System.Short _
) 
```

```

Dim instance As IGtol
Dim Composite As System.Boolean
Dim FrameNum As System.Short
 
instance.SetCompositeFrame2(Composite, FrameNum)
```

```

void SetCompositeFrame2( 
   System.bool Composite,
   System.short FrameNum
)
```

```

void SetCompositeFrame2( 
   System.bool Composite,
   System.short FrameNum
) 
```

#### Parameters

*Composite*
:   True to create a composite frame, false to not (see **Remarks**)

*FrameNum*
:   Index of GTol frame

Remarks

If Composite is true, this method creates a composite frame containing adjacent GTol frames:

- Frame with index FrameNum.
- Frame directly below.

Both GTol frames must have the same symbol.

Example

[Create GTol Composite Frame (VBA)](Create_Gtol_Composite_Frame_Example_VB.htm)  
[Create GTol Composite Frame (VB.NET)](Create_Gtol_Composite_Frame_Example_VBNET.htm)  
[Create GTol Composite Frame (C#)](Create_Gtol_Composite_Frame_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetCompositeFrame2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetCompositeFrame2.md)
