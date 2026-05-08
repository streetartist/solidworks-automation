# InsertBendTable Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBendTable`

Creates a bend table annotation for the flat pattern of this sheet metal part.
Creates a bend table annotation for the flat pattern of this sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBendTable( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal StartValue As System.String, _
   ByVal TableTemplate As System.String _
) As System.Object
```

```

Dim instance As IPartDoc
Dim X As System.Double
Dim Y As System.Double
Dim StartValue As System.String
Dim TableTemplate As System.String
Dim value As System.Object
 
value = instance.InsertBendTable(X, Y, StartValue, TableTemplate)
```

```

System.object InsertBendTable( 
   System.double X,
   System.double Y,
   System.string StartValue,
   System.string TableTemplate
)
```

```

System.Object^ InsertBendTable( 
   System.double X,
   System.double Y,
   System.String^ StartValue,
   System.String^ TableTemplate
) 
```

#### Parameters

*X*
:   X-coordinate for placement of the bend table

*Y*
:   Y-coordinate for placement of the bend table

*StartValue*
:   Starting datum tag; a value from A to Z for letter tags; a positive integer for number tags

*TableTemplate*
:   Full pathname of the template (e.g., *install\_dir*\**lang\***language**\*****bendtable-standard.sldbndtbt**)

#### Return Value

[IBendTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation.md)

Example

'VBA

'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

'1. Ensure the specified part and table template exist.  
'2. Run the macro.  
'3. Inserts a bend table annotation for the flat pattern.  
'4. Inspect the graphics area and the Immediate window.

'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Dim swApp As SldWorks.SldWorks  
Dim myBendTableAnno As SldWorks.BendTableAnnotation  
Dim myBendTable As SldWorks.BendTable  
Dim Part As SldWorks.ModelDoc2  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long  
Option Explicit  
Sub main()

> Set swApp = Application.SldWorks  
> Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\SMGussetAPI.SLDPRT", 1, 0, "", longstatus, longwarnings)  
> swApp.ActivateDoc2 "SMGussetAPI.SLDPRT", False, longstatus  
> Set Part = swApp.ActiveDoc  
>   
> Set myBendTableAnno = Part.**InsertBendTable**(-4.06616963665726E-02, 6.09432383467686E-02, "A", "install\_dir\lang\english\bendtable-standard.sldbndtbt")  
> Set myBendTable = myBendTableAnno.**BendTable**  
> Debug.Print "Tag style of the bend table as defined in swBendTableTagStyle\_e: " & myBendTable.TagStyle  
>   
> End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.md)  
[IView::InsertBendTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBendTable.md)
