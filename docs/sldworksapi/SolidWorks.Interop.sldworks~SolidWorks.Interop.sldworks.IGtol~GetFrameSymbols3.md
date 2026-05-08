# GetFrameSymbols3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols3`

Gets the symbols for the specified frame.
Gets the symbols for the specified frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFrameSymbols3( _
   ByVal FrameNumber As System.Integer _
) As System.Object
```

```

Dim instance As IGtol
Dim FrameNumber As System.Integer
Dim value As System.Object
 
value = instance.GetFrameSymbols3(FrameNumber)
```

```

System.object GetFrameSymbols3( 
   System.int FrameNumber
)
```

```

System.Object^ GetFrameSymbols3( 
   System.int FrameNumber
) 
```

#### Parameters

*FrameNumber*
:   Frame number to examine (1 or 2)

#### Return Value

Array of six strings (see **Remarks**)

Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

The return array is an array of six strings in the following format:

*retval*[0] = Geometric tolerance symbol

*retval*[1] = Material condition symbol for first tolerance value

*retval*[2] = Material condition symbol for second tolerance value

*retval*[3] = Material condition symbol for datum1

*retval*[4] = Material condition symbol for datum2

*retval*[5] = Material condition symbol for datum3

The character strings returned in the array correspond to symbols defined in **C:\ProgramData\SolidWorks\SolidWorks** **20***nn***\lang\english\gtol.sym**. The format of each string is <*LibraryName-SymbolName*> (for example, **<GTOL-ANGULAR>,** which is the angularity symbol from the ASME Geometric Tolerancing Symbols library).

Use this method with [IGtol::GetFrameDiameterSymbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.md), which determines whether diameter symbols are displayed.

Example

[Get Text Items in GTol Frame (C#)](Get_Text_Items_in_GTol_Frame_Example_CSharp.htm)  
[Get Text Items in GTol Frame (VB.NET)](Get_Text_Items_in_GTol_Frame_Example_VBNET.htm)  
[Get Text Items in GTol Frame (VBA)](Get_Text_Items_in_GTol_Frame_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetFrameCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.md)  
[IGtol::GetFrameDiameterSymbols Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols.md)  
[IGtol::IGetFrameDiameterSymbols Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameDiameterSymbols.md)  
[IGtol::GetFrameValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.md)  
[IGtol::IGetFrameValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.md)  
[IGtol::SetFrameSymbols2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.md)  
[IGtol::SetFrameValues2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues2.md)
