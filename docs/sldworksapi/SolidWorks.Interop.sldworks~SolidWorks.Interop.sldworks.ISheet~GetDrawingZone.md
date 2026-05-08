# GetDrawingZone Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetDrawingZone`

Gets the name of the drawing zone for the specified x and y coordinates on the sheet.
Gets the name of the drawing zone for the specified x and y coordinates on the sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDrawingZone( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.String
```

```

Dim instance As ISheet
Dim X As System.Double
Dim Y As System.Double
Dim value As System.String
 
value = instance.GetDrawingZone(X, Y)
```

```

System.string GetDrawingZone( 
   System.double X,
   System.double Y
)
```

```

System.String^ GetDrawingZone( 
   System.double X,
   System.double Y
) 
```

#### Parameters

*X*
:   x coordinate

*Y*
:   y coordinate

#### Return Value

Name of the drawing zone

Example

[Get Name of Drawing Zone (C#)](Get_Name_of_Drawing_Zone_Example_CSharp.htm)  
[Get Name of Drawing Zone (VB.NET)](Get_Name_of_Drawing_Zone_Example_VBNET.htm)  
[Get Name of Drawing Zone (VBA)](Get_Name_of_Drawing_Zone_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[IDrawingDoc::NewSheet4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet4.md)  
[IDrawingDoc::SetupSheet6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.md)
