# GetCompositeFrame2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetCompositeFrame2`

Gets whether the GTol frame with the specified index is part of a composite frame.
Gets whether the GTol frame with the specified index is part of a composite frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCompositeFrame2( _
   ByVal FrameNum As System.Short _
) As System.Boolean
```

```

Dim instance As IGtol
Dim FrameNum As System.Short
Dim value As System.Boolean
 
value = instance.GetCompositeFrame2(FrameNum)
```

```

System.bool GetCompositeFrame2( 
   System.short FrameNum
)
```

```

System.bool GetCompositeFrame2( 
   System.short FrameNum
) 
```

#### Parameters

*FrameNum*
:   Index of GTol frame

#### Return Value

True if GTol frame is part of a composite frame, false if not

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
[IGtol::SetCompositeFrame2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetCompositeFrame2.md)
