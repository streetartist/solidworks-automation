# GetFrameCount Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount`

Gets the number of frames in this GTol symbol.
Gets the number of frames in this GTol symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFrameCount() As System.Short
```

```

Dim instance As IGtol
Dim value As System.Short
 
value = instance.GetFrameCount()
```

```

System.short GetFrameCount()
```

```

System.short GetFrameCount(); 
```

#### Return Value

Number of frames in this GTol symbol

Remarks

This method returns the number of frames that this symbol has stored, which may be different than the number of frames that actually appear when this frame is displayed. This is because symbols can be created, either through the user interface or the API, with empty frames or rows, which do not appear when the frame is displayed.

For example, the symbol can be displayed with three 3 frames, but upon examination, it could be that those are frames 1, 2, and 5. Frames 3 and 4 are empty. Every symbol must have at least 2 frames.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Example

[Get Text Items in GTol Frame (VBA)](Get_Text_Items_in_GTol_Frame_VB.htm)  
[Get Text Items in GTol Frame (VB.NET)](Get_Text_Items_in_GTol_Frame_Example_VBNET.htm)  
[Get Text Items in GTol Frame (C#)](Get_Text_Items_in_GTol_Frame_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.md)  
[IGtol::GetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.md)  
[IGtol::GetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.md)  
[IGtol::IGetFrameDiameterSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.md)  
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.md)  
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.md)  
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.md)  
[IGtol::SetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.md)
